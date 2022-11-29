
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getFeaturedCompsThunk } from '../../store/comparisons';
import { getFeaturedSetsThunk } from '../../store/sets';
import SetCard from "../sets/SetCard"
import "./homepage.css"
const HomePage = () => {
    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)

    useEffect(() => {
        dispatch(getFeaturedSetsThunk()).then(() => dispatch(getFeaturedCompsThunk())).then(() => setIsLoaded(true))
    }, [dispatch])

    let featuredSets = useSelector((state) => {
        if (isLoaded && state.sets) return Object.values(state.sets)
        else return []
    })

    return (
        <>
            {isLoaded && <div className='homepage-wrapper'>
                <h2>Featured sets</h2>
                <div className='homepage-setcards-wrapper'>
                    {featuredSets?.map((set) => <SetCard set={set} key={set.id} />)}
                </div>
                <h2>Featured comparisons</h2>
                <div className='homepage-comparisons-wrapper'>

                </div>
            </div>}
        </>
    )
}

export default HomePage
