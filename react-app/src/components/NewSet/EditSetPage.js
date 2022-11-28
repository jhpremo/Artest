import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { clearSets, getOneSetThunk } from "../../store/sets"
import { formAddCard, formReset, loadEditList } from "../../store/setForm"
import EditCard from "./EditCard"
import "./new-set.css"

const EditSetPage = () => {
    const [setTitle, setSetTitle] = useState('')
    const [errors, setErrors] = useState([])
    const cards = useSelector((state) => state.setForm)
    const [isLoaded, setIsLoaded] = useState(false)
    const history = useHistory()
    const dispatch = useDispatch()
    const { setId } = useParams()

    let set = useSelector((state) => {
        if (state.sets) return state.sets[setId]
        else return null
    })

    useEffect(() => {
        if (!set) {
            dispatch(getOneSetThunk(setId)).then((res) => {
                if (res) setIsLoaded(true)
                else history.push('/404')
            })
        } else {
            dispatch(formReset())
            setSetTitle(set.title)
            dispatch(loadEditList(set.cards))
            setIsLoaded(true)
        }
    }, [set, dispatch, history, setId])

    const user = useSelector((state) => state.session.user)
    useEffect(() => {
        if (isLoaded && (!user || user?.id != set?.userId)) {
            history.push('/')
            return
        }
    }, [history, user, isLoaded])

    const addCard = () => {
        dispatch(formAddCard())
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        let errorsArr = []

        if (!setTitle || setTitle.length > 75) errorsArr.push('Set title must be between 1 and 75 characters')

        for (let i = 0; i < cards.length; i++) {
            let card = cards[i]
            if (!card.title || card.title.length > 75) errorsArr.push(`Card ${i + 1} title must be between 1 and 75 characters`)
            if (!card.artist || card.artist.length > 75) errorsArr.push(`Card ${i + 1} artist name must be between 1 and 75 characters`)
            if (!card.displayDate || card.displayDate.length > 75) errorsArr.push(`Card ${i + 1} date must be between 1 and 50 characters`)
            if (!card.imageUrl || card.imageUrl.length > 2048 || !(card.imageUrl.includes('.jpg') || card.imageUrl.includes('.png'))) errorsArr.push(`Card ${i + 1} image url must be valid url that includes .jpg or .png`)
            if (card.notes && card.notes.length > 1000) errorsArr.push(`Card ${i + 1} notes must be less than 1000 characters`)
        }
        console.log(errorsArr)
        if (errorsArr.length) {
            setErrors(errorsArr)
            return
        }


        const response = await fetch(`/api/sets/${set.id}`, {
            method: 'put',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: setTitle
            })
        })

        if (response.ok) {
            const editedSet = await response.json()
            let nonDeletedCardIds = []
            for (let i = 0; i < cards.length; i++) {
                let card = cards[i]
                if (card.id) {
                    await fetch(`/api/cards/${card.id}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            title: card.title,
                            artist: card.artist,
                            image_url: card.imageUrl,
                            display_date: card.displayDate,
                            notes: card.notes
                        })
                    })
                    nonDeletedCardIds.push(card.id)
                } else {
                    await fetch(`/api/sets/${set.id}/cards`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            title: card.title,
                            artist: card.artist,
                            image_url: card.imageUrl,
                            display_date: card.displayDate,
                            notes: card.notes
                        })
                    })
                }
            }
            let deletedCards = set.cards.filter((card) => {
                let deleted = true
                if (nonDeletedCardIds.includes(card.id)) {
                    deleted = false
                }
                return deleted
            })

            for (let i = 0; i < deletedCards.length; i++) {
                let deletedCard = deletedCards[i]
                await fetch(`/api/cards/${deletedCard.id}`, {
                    method: 'DELETE'
                })
            }
            setIsLoaded(false)
            await dispatch(clearSets())
            await dispatch(formReset())
            history.push(`/sets/${set.id}`)
        }
    }


    return (
        <>{isLoaded && <div className="new-set-page-wrapper">
            <h2>Edit {set.title}</h2>
            <form onSubmit={handleSubmit} className="new-set-form">
                {errors.length > 0 && <ul className="form-errors">
                    {errors.map((error, idx) => <li key={idx}>{error}</li>)}
                </ul>}
                <div className="new-set-input-wrapper">
                    <input
                        type="text"
                        className="create-form-input"
                        value={setTitle}
                        onChange={(e) => setSetTitle(e.target.value)}
                        required
                        maxLength={75}
                    />
                    <span className="create-form-label">
                        Set title
                    </span>
                </div>
                {cards.map((card, i) => <EditCard index={i} isLoaded={isLoaded} />)}

                <button type="button" onClick={addCard} className='form-add-card-button'>+ Add Card</button>
                <button className="form-submit-button">Done</button>
            </form>
        </div>}
        </>
    )
}

export default EditSetPage
