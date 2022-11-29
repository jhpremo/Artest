import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from "react-router-dom"
import { getSessionCompsThunk } from '../../store/comparisons';
import CompCard from '../CompCard/CompCard';


const YourComps = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setIsLoaded] = useState(false)
    const user = useSelector((state) => state.session.user)
    useEffect(() => {
        if (!user) {
            history.push('/')
            return
        }
        dispatch(getSessionCompsThunk()).then(() => setIsLoaded(true))
    }, [dispatch, history, user])

    let sessionComps = useSelector((state) => {
        if (isLoaded && state.comparisons) return Object.values(state.comparisons)
        else return []
    })

    return (
        <>
            {isLoaded && <div className='homepage-wrapper'>
                <h2>Your Sets</h2>
                <div className='homepage-comparisons-wrapper'>
                    {sessionComps?.map((comp) => <CompCard comp={comp} key={comp.id} />)}
                </div>
            </div>}
        </>
    )
}

export default YourComps
