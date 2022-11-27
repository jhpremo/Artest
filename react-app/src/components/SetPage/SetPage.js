import { useState } from "react"
import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { getOneSetThunk } from "../../store/sets"
import NewCard from "../NewSet/NewCard"
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
    const [shuffleId, setShuffleId] = useState("n/a")
    const [defaultId, setDefaultId] = useState("active-side-button")
    const { setId } = useParams()
    const user = useSelector((state) => state.session.user)

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
    }, [set, dispatch, history, setId])



    const handleLeft = (e) => {
        e.stopPropagation()
        if (toggleDefaultSide) setTogglePaintingSide(true)
        else setTogglePaintingSide(false)
        if (currentCard === 0) setCurrentCard(displayLst.length - 1)
        else setCurrentCard(currentCard - 1)
        console.log(currentCard)
    }

    const handleRight = (e) => {
        e.stopPropagation()
        if (toggleDefaultSide) setTogglePaintingSide(true)
        else setTogglePaintingSide(false)
        if (currentCard === displayLst.length - 1) setCurrentCard(0)
        else setCurrentCard(currentCard + 1)
    }
    const handleShuffle = () => {
        let shuffledList = [...set.cards]
        if (!toggleShuffle) {
            setShuffleId("active-shuffle")
            for (let i = shuffledList.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1))
                const placeHolder = shuffledList[i]
                shuffledList[i] = shuffledList[j]
                shuffledList[j] = placeHolder
            }
        } else setShuffleId("n/a")
        setDisplayLst(shuffledList)
        setToggleShuffle(!toggleShuffle)
    }

    const handleDefaultSide = () => {
        if (!toggleDefaultSide) {
            setDefaultId('active-side-button')
            setTogglePaintingSide(true)
        } else {
            setDefaultId('n/a')
            setTogglePaintingSide(false)
        }

        setToggleDefaultSide(!toggleDefaultSide)
    }

    return (
        <>
            {isLoaded && <div className="set-page-wrapper">
                <h1>{set.title}</h1>
                {displayLst.length > 0 && <>
                    <div className="progress-bar">
                        <div className="progress-bar-inner" style={{ width: `${((currentCard + 1) / displayLst.length) * 100}%` }}></div>
                    </div>
                    <div onClick={() => setTogglePaintingSide(!togglePaintingSide)} className='set-page-card-wrapper'>
                        <div className="card-counter">{currentCard + 1} / {displayLst.length}</div>
                        {togglePaintingSide &&
                            <img
                                className="set-page-card-image"
                                alt={displayLst[currentCard].title}
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
                            <button onClick={handleShuffle} id={shuffleId}><i className="fa-solid fa-shuffle" /></button>
                            <button onClick={handleDefaultSide} id={defaultId}><i className="fa-regular fa-image" /></button>
                        </div>
                    </div></>}
                <div className="cards-list-wrapper">
                    {set.cards.map(card => {
                        return (
                            <div className="cards-list-card">
                                <div className='cards-list-card-left'>
                                    <p>{card.title}</p>
                                    <p>{card.displayDate}</p>
                                    <p>{card.artist}</p>
                                    {card.notes !== null && <p> Notes: {card.notes}</p>}
                                </div>
                                <div className='cards-list-card-right'>
                                    <img
                                        className="set-page-card-list-image"
                                        alt={card.title}
                                        src={card.imageUrl}
                                        onError={e => {
                                            e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                            e.onerror = null
                                        }}
                                    ></img>
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>}
        </>
    )
}

export default SetPage
