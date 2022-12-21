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
    const [toggleList, setToggleList] = useState(true)
    const [toggleAbout, setToggleAbout] = useState(false)
    const [currentCard, setCurrentCard] = useState(0)
    const [shuffleId, setShuffleId] = useState("n/a")
    const [defaultId, setDefaultId] = useState("active-side-button")
    const [listId, setListId] = useState("active-list-button")
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

    const handleListToggle = () => {
        if (!toggleList) {
            setListId('active-list-button')
            setToggleList(true)
        } else {
            setListId('n/a')
            setToggleList(false)
        }
    }

    const handleDeleteSet = async () => {
        if (
            window.confirm(
                `This will delete ${set.title} and all associated cards`
            )
        ) {
            await fetch(`/api/sets/${set.id}`, {
                method: "DELETE"
            })
            history.push('/your-sets')
        }
    }

    const handleEditSet = () => {
        history.push(`/sets/${set.id}/edit`)
    }

    useEffect(() => {
        if (!toggleAbout) return;

        const closeAbout = () => {
            setToggleAbout(false);
        };

        document.addEventListener('click', closeAbout);

        return () => document.removeEventListener("click", closeAbout);
    }, [toggleAbout]);


    return (
        <>
            {isLoaded && <div className="set-page-wrapper">
                <div className="set-page-top-bar">
                    <h1>{set.title}</h1>
                    <div className="set-page-top-bar-buttons">
                        {user?.id === set.userId && <button onClick={handleEditSet}>edit</button>}
                        {user?.id === set.userId && <button onClick={handleDeleteSet}>delete</button>}
                        <button onClick={() => setToggleAbout(!toggleAbout)} id='set-page-about' className='about-this-page-button'>about</button>
                        {toggleAbout && <div className='about-drop-down'>
                            <h5>Welcome to Artest an Art History Flash Card and Study Site</h5>
                            <div className='about-section-wrapper'>
                                <h6>Sets</h6>
                                <p>Sets are collections of flash cards where one side features a work of art and the other shows the artist, year, and title for the work of art. The creator of a set can also write and display notes on each card.</p>
                            </div>
                            <div className='about-section-wrapper'>
                                <h6>Set Page</h6>
                                <p><ul>
                                    <li>Clicking on the card will flip the card</li>
                                    <li><i className="fa-solid fa-angle-right" /> will move to next card in set</li>
                                    <li><i className="fa-solid fa-angle-left" /> will move to previous card in set</li>
                                    <li><i className="fa-solid fa-list-ul" /> will toggle visibility for the card list</li>
                                    <li><i className="fa-solid fa-shuffle" /> will toggle randomized card order</li>
                                    <li><i className="fa-regular fa-image" /> will toggle the starting card side </li>
                                </ul></p>
                            </div>
                        </div>}
                    </div>
                </div>
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
                                    e.target.src = "https://artest-project.s3.amazonaws.com/No_Image_Available.jpg"
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
                            <button onClick={handleListToggle} id={listId}><i className="fa-solid fa-list-ul" /></button>
                            <button onClick={handleShuffle} id={shuffleId}><i className="fa-solid fa-shuffle" /></button>
                            <button onClick={handleDefaultSide} id={defaultId}><i className="fa-regular fa-image" /></button>
                        </div>
                    </div></>}
                {toggleList && <div className="cards-list-wrapper">
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
                                            e.target.src = "https://artest-project.s3.amazonaws.com/No_Image_Available.jpg"
                                            e.onerror = null
                                        }}
                                    ></img>
                                </div>
                            </div>
                        )
                    })}
                </div>}
            </div>}
        </>
    )
}

export default SetPage
