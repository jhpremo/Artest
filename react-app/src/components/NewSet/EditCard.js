import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { formDeleteCard, updateListItem } from "../../store/setForm"

const NewCard = ({ index, isLoaded }) => {
    const dispatch = useDispatch()
    const [title, setTitle] = useState('')
    const [artist, setArtist] = useState('')
    const [displayDate, setDisplayDate] = useState('')
    const [url, setUrl] = useState('')
    const [notes, setNotes] = useState('')
    const [disableDelete, setDisableDelete] = useState(false)

    const cards = useSelector((state) => state.setForm)

    useEffect(() => {
        let cardObj = {
            title,
            artist,
            displayDate,
            imageUrl: url,
            notes,
            id: cards[index].id
        }

        dispatch(updateListItem(cardObj, index))

    }, [title, artist, displayDate, url, notes, index, dispatch])

    useEffect(() => {
        setTitle(cards[index].title)
        setArtist(cards[index].artist)
        setDisplayDate(cards[index].displayDate)
        setUrl(cards[index].imageUrl)
        setNotes(cards[index].notes)

        if (cards.length > 2) setDisableDelete(false)
        else setDisableDelete(true)

    }, [cards.length, isLoaded])

    const deleteCard = () => {
        if (cards.length > 2) dispatch(formDeleteCard(index))
    }



    return (
        <div className="form-cards-list-card-wrapper">
            <div className="card-num-wrapper"><div>{index + 1}</div> <button type="button" disabled={disableDelete} onClick={deleteCard}><i className="fa-solid fa-trash-can" /></button> </div>
            <div className="form-cards-list-card">
                <div className='form-cards-list-card-left'>
                    <div className="new-card-input-wrapper">
                        <input
                            type="text"
                            className="create-form-card-input"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            required
                            maxLength={75}
                        />
                        <span className="create-form-card-label">
                            Title e.g "Hades abducting persephone amphora"
                        </span>
                    </div>
                    <div className="new-card-input-wrapper">
                        <input
                            type="text"
                            className="create-form-card-input"
                            value={artist}
                            onChange={(e) => setArtist(e.target.value)}
                            required
                            maxLength={75}
                        />
                        <span className="create-form-card-label">
                            Artist name e.g "Andokides Painter"
                        </span>
                    </div>
                    <div className="new-card-input-wrapper">
                        <input
                            type="text"
                            className="create-form-card-input"
                            value={displayDate}
                            onChange={(e) => setDisplayDate(e.target.value)}
                            required
                            maxLength={50}
                        />
                        <span className="create-form-card-label">
                            Display Date e.g "6th century B.C.E."
                        </span>
                    </div>
                    <div className="new-card-input-wrapper">
                        <input
                            type="text"
                            className="create-form-card-input"
                            value={url}
                            onChange={(e) => setUrl(e.target.value)}
                            required
                            maxLength={2048}
                        />
                        <span className="create-form-card-label">
                            Image url
                        </span>
                    </div>
                    <div className="new-card-input-wrapper">
                        <textarea
                            className="create-form-card-input-text-area"
                            onChange={e => setNotes(e.target.value)}
                            value={notes}
                            minLength={1}
                            maxLength={1000}
                        />
                        <span className="create-form-card-label">
                            Notes
                        </span>
                    </div>
                </div>
                <div className='form-cards-list-card-right'>
                    <img
                        className="form-set-page-card-list-image"
                        alt={title}
                        src={url}
                        onError={e => {
                            e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                            e.onerror = null
                        }}
                    ></img>
                </div>
            </div>
        </div>
    )
}

export default NewCard
