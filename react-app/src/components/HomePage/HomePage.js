
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getFeaturedSetsThunk } from '../../store/sets';
import SetCard from "../sets/SetCard"
import "./homepage.css"
const HomePage = () => {
    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)

    useEffect(() => {
        dispatch(getFeaturedSetsThunk()).then(() => setIsLoaded(true))
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
            </div>}
        </>
    )
}

export default HomePage
