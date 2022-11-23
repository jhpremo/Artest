const SetCard = ({ set }) => {
    return (
        <div className="set-card-wrapper">
            <h3>{set.title}</h3>
            <h4>Created by {set.username}</h4>
            <h5>{set.numCards} cards</h5>
        </div>
    )
}

export default SetCard
