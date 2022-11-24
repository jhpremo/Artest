import { useState } from "react"
import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { getOneSetThunk } from "../../store/sets"
import "./set-page.css"

const SetPage = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setIsLoaded] = useState(false)
    const [displayLst, setDisplayLst] = useState([])
    const [togglePaintingSide, setTogglePaintingSide] = useState(true)
    const [toggleShuffle, setToggleShuffle] = useState(false)
    const [toggleDefaultSide, setToggleDefaultSide] = useState(true)
    const [currentCard, setCurrentCard] = useState(0)
    const { setId } = useParams()

    let set = useSelector((state) => {
        if (state.sets) return state.sets[setId]
        else return null
    })

    useEffect(() => {
        if (!set) {
            dispatch(getOneSetThunk(setId)).then((res) => {
                if (res) setIsLoaded(true)
                else history.push('/404')
            })
        } else setIsLoaded(true)
        setDisplayLst(set?.cards)
    }, [set])

    const handleLeft = (e) => {
        e.stopPropagation()
        setTogglePaintingSide(true)
        if (currentCard === 0) setCurrentCard(displayLst.length - 1)
        else setCurrentCard(currentCard - 1)
        console.log(currentCard)
    }

    const handleRight = (e) => {
        e.stopPropagation()
        setTogglePaintingSide(true)
        if (currentCard === displayLst.length - 1) setCurrentCard(0)
        else setCurrentCard(currentCard + 1)
    }

    const handleShuffle = () => {
        setToggleShuffle(!toggleShuffle)
    }

    const handleDefaultSide = () => {
        setToggleDefaultSide(!toggleDefaultSide)
    }

    return (
        <>
            {isLoaded && <div className="set-page-wrapper">
                <h1>{set.title}</h1>
                <div className="progress-bar">
                    <div className="progress-bar-inner" style={{ width: `${((currentCard + 1) / displayLst.length) * 100}%` }}></div>
                </div>
                <div onClick={() => setTogglePaintingSide(!togglePaintingSide)} className='set-page-card-wrapper'>
                    <div className="card-counter">{currentCard + 1} / {displayLst.length}</div>
                    {togglePaintingSide &&
                        <img
                            className="set-page-card-image"
                            src={displayLst[currentCard].imageUrl}
                            onError={e => {
                                e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                e.onerror = null
                            }}
                        ></img>}
                    {!togglePaintingSide &&
                        <div className="set-page-card-info">
                            <h3>{displayLst[currentCard].title}</h3>
                            <h4>{displayLst[currentCard].artist}</h4>
                            <h5>{displayLst[currentCard].displayDate}</h5>
                            {displayLst[currentCard].notes !== null && <p> Notes: {displayLst[currentCard].notes}</p>}
                        </div>
                    }
                    <div className="arrow-button-wrapper">
                        <button className="arrow-button" onClick={handleLeft}><i className="fa-solid fa-angle-left" /></button>
                        <button className="arrow-button" onClick={handleRight}><i className="fa-solid fa-angle-right" /></button>
                    </div>
                </div>
                <div className="below-card-wrapper">
                    <p>Created by {set.username}</p>
                    <div className='set-options-button-wrapper'>
                        <button onClick={handleShuffle} id={toggleShuffle && "active-shuffle"}><i className="fa-solid fa-shuffle" /></button>
                        <button onClick={handleDefaultSide} id={toggleDefaultSide && "active-side-button"}><i className="fa-regular fa-image" /></button>
                    </div>
                </div>
            </div>}
        </>
    )
}

export default SetPage
