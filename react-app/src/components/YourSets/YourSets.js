import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from "react-router-dom"
import { getSessionSetsThunk } from '../../store/sets';
import SetCard from "../sets/SetCard"


const YourSets = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setIsLoaded] = useState(false)
    const user = useSelector((state) => state.session.user)
    useEffect(() => {
        if (!user) {
            history.push('/')
            return
        }
        dispatch(getSessionSetsThunk()).then(() => setIsLoaded(true))
    }, [dispatch])

    let sessionSets = useSelector((state) => {
        if (isLoaded && state.sets) return Object.values(state.sets)
        else return []
    })

    return (
        <>
            {isLoaded && <div className='homepage-wrapper'>
                <h2>Your Sets</h2>
                <div className='homepage-setcards-wrapper'>
                    {sessionSets?.map((set) => <SetCard set={set} key={set.id} />)}
                </div>
            </div>}
        </>
    )
}

export default YourSets
