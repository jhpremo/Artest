import { useHistory } from "react-router-dom"

const CompCard = ({ comp }) => {
    const history = useHistory()
    return (
        <div onClick={() => history.push(`/comparisons/${comp.id}`)} className="comp-card-wrapper">
            <div className="comp-card-top">
                <img
                    src={comp.workOneImageUrl}
                    alt={comp.workOneTitle}
                    id="comp-card-image-left"
                    onError={e => {
                        e.target.src = "https://artest-project.s3.amazonaws.com/No_Image_Available.jpg"
                        e.onerror = null
                    }} />
                <img
                    src={comp.workTwoImageUrl}
                    alt={comp.workTwoTitle}
                    onError={e => {
                        e.target.src = "https://artest-project.s3.amazonaws.com/No_Image_Available.jpg"
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
