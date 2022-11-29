import { useHistory } from "react-router-dom"

const CompCard = ({ comp }) => {
    const history = useHistory()
    return (
        <div onClick={() => history.push(`/comp/${comp.id}`)} className="comp-card-wrapper">
            <div className="comp-card-top">
                <img
                    src={comp.workOneImageUrl}
                    alt={comp.workOneTitle}
                    id="comp-card-image-left"
                    onError={e => {
                        e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                        e.onerror = null
                    }} />
                <img
                    src={comp.workTwoImageUrl}
                    alt={comp.workTwoTitle}
                    onError={e => {
                        e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                        e.onerror = null
                    }} />
                <div className="comp-card-work-wrapper"></div>
            </div>
            <div className="comp-card-bottom">
                <h3>{comp.title}</h3>
                <h4>Comparison by {comp.username}</h4>
            </div>
        </div>
    )
}

export default CompCard
