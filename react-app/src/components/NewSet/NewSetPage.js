import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { formAddCard } from "../../store/setForm"
import NewCard from "./NewCard"

const NewSetPage = () => {
    const [setTitle, setSetTitle] = useState('')
    const [submitted, setSubmitted] = useState(false)
    const cards = useSelector((state) => state.setForm)
    const dispatch = useDispatch()

    const addCard = () => {
        dispatch(formAddCard())
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
    }

    return (
        <div className="new-set-page-wrapper">
            <h2>Create a new art set</h2>
            <form onSubmit={handleSubmit}>
                <div className="new-set-title-wrapper">
                    <label >
                        Set title
                    </label>
                    <input
                        type="text"
                        value={setTitle}
                        onChange={(e) => setSetTitle(e.target.value)}
                        required
                        maxLength={75}
                    />
                </div>
                {cards.map((card, i) => <NewCard index={i} />)}

                <button type="button" onClick={addCard} >Add card</button>
                <button>Create</button>
            </form>
        </div>
    )
}

export default NewSetPage
