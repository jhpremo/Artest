
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getFeaturedCompsThunk } from '../../store/comparisons';
import { getFeaturedSetsThunk } from '../../store/sets';
import SetCard from "../sets/SetCard"
import CompCard from '../CompCard/CompCard';
import "./homepage.css"

const HomePage = () => {
    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)
    const user = useSelector((state) => state.session.user)
    useEffect(() => {
        dispatch(getFeaturedSetsThunk()).then(() => dispatch(getFeaturedCompsThunk())).then(() => setIsLoaded(true))
    }, [dispatch])

    let featuredSets = useSelector((state) => {
        if (isLoaded && state.sets) return Object.values(state.sets)
        else return []
    })

    let featuredComps = useSelector((state) => {
        if (isLoaded && state.comparisons) return Object.values(state.comparisons)
        else return []
    })

    return (
        <>
            {isLoaded && <div className='homepage-wrapper'>
                {!user && < div className='welcome-message'>Welcome to Artest an Art History Flash Card and Study Site</div>}
                <h2>Featured sets</h2>
                <div className='homepage-setcards-wrapper'>
                    {featuredSets?.map((set) => <SetCard set={set} key={set.id} />)}
                </div>
                <h2>Featured comparisons</h2>
                <div className='homepage-comparisons-wrapper'>
                    {featuredComps?.map((comp) => <CompCard comp={comp} key={comp.id} />)}
                </div>
            </div>}
        </>
    )
}

export default HomePage
