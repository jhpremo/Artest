import { useState } from "react"
import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { getOneCompThunk } from "../../store/comparisons"
import "./comp-page.css"



const CompPage = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const user = useSelector((state) => state.session.user)
    const [isLoaded, setIsLoaded] = useState(false)
    const { compId } = useParams()

    let comp = useSelector((state) => {
        if (state.comparisons) return state.comparisons[compId]
        else return null
    })

    useEffect(() => {
        if (!comp) {
            dispatch(getOneCompThunk(compId)).then((res) => {
                if (res) setIsLoaded(true)
                else history.push('/404')
            })
        } else setIsLoaded(true)
    }, [comp, dispatch, history, compId])

    const handleDeleteSet = async () => {
        if (
            window.confirm(
                `This will delete ${comp.title}`
            )
        ) {
            await fetch(`/api/comparisons/${comp.id}`, {
                method: "DELETE"
            })
            history.push('/your-comparisons')
        }
    }

    const handleEditSet = () => {
        history.push(`/comparisons/${comp.id}/edit`)
    }

    return (
        <>
            {isLoaded && <div className="comp-page-wrapper">
                <div className="comp-page-top">
                    <div className="comp-page-work-wrapper" id="work-one">
                        <div className="comp-page-work-border">
                            <img
                                src={comp.workOneImageUrl}
                                alt={comp.workOneTitle}
                                onError={e => {
                                    e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                    e.onerror = null
                                }} />
                            <h3>{comp.workOneTitle}</h3>
                            <h3>{comp.workOneArtist}</h3>
                            <h3>{comp.workOneDisplayDate}</h3>
                        </div>
                    </div>
                    <div className="comp-page-work-wrapper" id="work-two">
                        <div className="comp-page-work-border">
                            <img
                                src={comp.workTwoImageUrl}
                                alt={comp.workTwoTitle}
                                onError={e => {
                                    e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                    e.onerror = null
                                }} />

                            <h3>{comp.workTwoTitle}</h3>
                            <h3>{comp.workTwoArtist}</h3>
                            <h3>{comp.workTwoDisplayDate}</h3>
                        </div>
                    </div>
                </div>
                <div className="comp-page-bottom">
                    <h4>{comp.title}</h4>
                    <p>{comp.comparisonText}</p>
                </div>
                {user?.id === comp.userId && <div className="set-page-top-bar-buttons" id="comp-page-bottom-button-wrapper">
                    <button onClick={handleEditSet}>edit</button>
                    <button onClick={handleDeleteSet}>delete</button>
                </div>}
            </div>}
        </>
    )
}


export default CompPage
