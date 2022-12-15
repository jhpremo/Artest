import React from "react"
import { useState } from "react"
import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { getOneCompThunk, updateMarkerThunk } from "../../store/comparisons"
import * as markerjs2 from 'markerjs2'
import "./comp-page.css"



const CompPage = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const user = useSelector((state) => state.session.user)
    const [isLoaded, setIsLoaded] = useState(false)
    const { compId } = useParams()
    const [showAnnotations, setShowAnnotations] = useState(false)
    const [imageCursor, setImageCursor] = useState({ cursor: 'default' })

    const showMarkerArea = (id) => {
        if (user?.id !== comp.userId) {
            if (showAnnotations) toggleDrawings()
        }
        else if (showAnnotations) {
            let markerArea = new markerjs2.MarkerArea(document.getElementById(id))
            markerArea.renderAtNaturalSize = true
            markerArea.addEventListener('render', async e => {
                await dispatch(updateMarkerThunk(compId, e.state, id))
                document.getElementById(id).src = e.dataUrl
            })
            markerArea.addEventListener('close', async e => {
                let markerArea = new markerjs2.MarkerArea(document.getElementById(id))
                markerArea.renderAtNaturalSize = true
                markerArea.addEventListener('render', async e => {
                    document.getElementById(id).src = e.dataUrl
                })
                if (id === "img1") markerArea.renderState(JSON.parse(comp.workOneMarkerObj))
                else if (id === "img2") markerArea.renderState(JSON.parse(comp.workTwoMarkerObj))

            })
            markerArea.show()
            if (id === "img1" && comp.workOneMarkerObj && comp.workOneMarkerObj != 'null') markerArea.restoreState(JSON.parse(comp.workOneMarkerObj))
            if (id === "img2" && comp.workTwoMarkerObj && comp.workTwoMarkerObj != 'null') markerArea.restoreState(JSON.parse(comp.workTwoMarkerObj))
        }
    }


    let comp = useSelector((state) => {
        if (state.comparisons) return state.comparisons[compId]
        else return null
    })

    const toggleDrawings = () => {
        if (showAnnotations) {
            document.getElementById("img1").src = comp.workOneImageUrl
            document.getElementById("img2").src = comp.workTwoImageUrl
            setImageCursor({ cursor: 'default' })
            setShowAnnotations(false)
        } else {
            if (comp.workOneMarkerObj && comp.workOneMarkerObj !== 'null') {
                let markerArea = new markerjs2.MarkerArea(document.getElementById("img1"))
                markerArea.renderAtNaturalSize = true
                markerArea.focus = null
                markerArea.addEventListener('render', async e => {
                    document.getElementById("img1").src = e.dataUrl
                })
                markerArea.renderState(JSON.parse(comp.workOneMarkerObj))
            }
            if (comp.workTwoMarkerObj && comp.workTwoMarkerObj !== 'null') {
                let markerArea = new markerjs2.MarkerArea(document.getElementById("img2"))
                markerArea.renderAtNaturalSize = true
                markerArea.addEventListener('render', async e => {
                    document.getElementById("img2").src = e.dataUrl
                })
                markerArea.renderState(JSON.parse(comp.workTwoMarkerObj))
            }
            setImageCursor({ cursor: 'pointer' })
            setShowAnnotations(true)
        }
    }

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
                                id="img1"
                                crossOrigin="anonymous"
                                onClick={(e) => {
                                    e.target.src = comp.workOneImageUrl
                                    showMarkerArea('img1')
                                }}
                                src={comp.workOneImageUrl}
                                style={imageCursor}
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
                                id="img2"
                                crossOrigin="anonymous"
                                onClick={(e) => {
                                    e.target.src = comp.workTwoImageUrl
                                    showMarkerArea('img2')
                                }}
                                src={comp.workTwoImageUrl}
                                style={imageCursor}
                                alt={comp.workTwoTitle}
                                onError={e => {
                                    e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                    e.onerror = null
                                }}></img>

                            <h3>{comp.workTwoTitle}</h3>
                            <h3>{comp.workTwoArtist}</h3>
                            <h3>{comp.workTwoDisplayDate}</h3>
                        </div>
                    </div>
                </div>
                <div className="comp-page-bottom">
                    <div>
                        <h4>{comp.title} </h4>
                        {showAnnotations && <button className="show-annotations" onClick={toggleDrawings}>hide annotations</button>}
                        {!showAnnotations && <button className="show-annotations" onClick={toggleDrawings}>show annotations</button>}
                    </div>
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
