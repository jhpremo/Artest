import { useHistory } from "react-router-dom"

const SetCard = ({ set }) => {
    const history = useHistory()
    return (
        <div onClick={() => history.push(`/sets/${set.id}`)} className="set-card-wrapper">
            <h3>{set.title}</h3>
            <h5>{set.numCards} cards</h5>
            <h4>Set by {set.username}</h4>
        </div>
    )
}

export default SetCard
