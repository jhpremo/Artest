
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getFeaturedSetsThunk } from '../../store/sets';

const HomePage = () => {
    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)
    useEffect(async () => {
        await dispatch(getFeaturedSetsThunk())
        setIsLoaded(true)
    }, [])

    return (
        <>
            {isLoaded && <div className='homepage-wrapper'>

            </div>}
        </>
    )
}

export default HomePage
