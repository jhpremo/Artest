import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"
import { formAddCard, formReset } from "../../store/setForm"
import NewCard from "./NewCard"
import "./new-set.css"

const NewSetPage = () => {
    const [setTitle, setSetTitle] = useState('')
    const [errors, setErrors] = useState([])
    const cards = useSelector((state) => state.setForm)
    const history = useHistory()
    const dispatch = useDispatch()

    const user = useSelector((state) => state.session.user)
    useEffect(() => {
        if (!user) {
            history.push('/')
            return
        }
    }, [history, user])

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
            if (!card.url || card.url.length > 2048 || !(card.url.includes('.jpg') || card.url.includes('.png'))) errorsArr.push(`Card ${i + 1} image url must be valid url that includes .jpg or .png`)
            if (card.notes && card.notes.length > 1000) errorsArr.push(`Card ${i + 1} notes must be less than 1000 characters`)
        }
        console.log(errorsArr)
        if (errorsArr.length) {
            setErrors(errorsArr)
            return
        }


        const response = await fetch('/api/sets', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: setTitle
            })
        })

        if (response.ok) {
            const set = await response.json()
            for (let i = 0; i < cards.length; i++) {
                let card = cards[i]
                await fetch(`/api/sets/${set.id}/cards`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        title: card.title,
                        artist: card.artist,
                        image_url: card.url,
                        display_date: card.displayDate,
                        notes: card.notes
                    })
                })
            }
            await dispatch(formReset())
            history.push(`/sets/${set.id}`)
        }
    }

    return (
        <div className="new-set-page-wrapper">
            <h2>Create a new art set</h2>
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
                {cards.map((card, i) => <NewCard index={i} />)}

                <button type="button" onClick={addCard} className='form-add-card-button'>+ Add Card</button>
                <button className="form-submit-button">Create</button>
            </form>
        </div>
    )
}

export default NewSetPage
