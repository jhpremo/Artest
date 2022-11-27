import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { formDeleteCard, updateListItem } from "../../store/setForm"

const NewCard = ({ index }) => {
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
            url,
            notes
        }

        dispatch(updateListItem(cardObj, index))

    }, [title, artist, displayDate, url, notes, index, dispatch])

    useEffect(() => {
        setTitle(cards[index].title)
        setArtist(cards[index].artist)
        setDisplayDate(cards[index].displayDate)
        setUrl(cards[index].url)
        setNotes(cards[index].notes)

        if (cards.length > 2) setDisableDelete(false)
        else setDisableDelete(true)

    }, [cards.length])

    const deleteCard = () => {
        if (cards.length > 2) dispatch(formDeleteCard(index))
    }



    return (
        <div className="cards-list-card">
            <div className='cards-list-card-left'>
                <div><div>{index + 1}</div> <button type="button" disabled={disableDelete} onClick={deleteCard}>trash</button> </div>
                <div className="new-card-input-wrapper">
                    <label >
                        Title
                    </label>
                    <input
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                        maxLength={75}
                    />
                </div>
                <div className="new-card-input-wrapper">
                    <label >
                        Artist
                    </label>
                    <input
                        type="text"
                        value={artist}
                        onChange={(e) => setArtist(e.target.value)}
                        required
                        maxLength={75}
                    />
                </div>
                <div className="new-card-input-wrapper">
                    <label >
                        Date
                    </label>
                    <input
                        type="text"
                        value={displayDate}
                        onChange={(e) => setDisplayDate(e.target.value)}
                        required
                        maxLength={50}
                    />
                </div>
                <div className="new-card-input-wrapper">
                    <label >
                        Image url
                    </label>
                    <input
                        type="text"
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        required
                        maxLength={2048}
                    />
                </div>
                <div>
                    <label>Notes</label>
                    <textarea
                        onChange={e => setNotes(e.target.value)}
                        value={notes}
                        maxLength={1000}
                    />
                </div>
            </div>
            <div className='cards-list-card-right'>
                <img
                    className="set-page-card-list-image"
                    alt={title}
                    src={url}
                    onError={e => {
                        e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                        e.onerror = null
                    }}
                ></img>
            </div>
        </div>
    )
}

export default NewCard
