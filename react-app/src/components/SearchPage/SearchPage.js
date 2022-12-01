import { useState } from "react"
import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useLocation } from "react-router-dom"
import { getOneSetThunk, getSearchSetsThunk } from "../../store/sets"
import SetCard from "../sets/SetCard"
import CompCard from '../CompCard/CompCard';
import { getSearchCompsThunk } from "../../store/comparisons"

const SearchPage = () => {
    const dispatch = useDispatch()
    const location = useLocation()
    const [isLoaded, setIsLoaded] = useState(false)
    const [topResults, setTopResults] = useState(true)
    const [setResults, setSetResults] = useState(false)
    const [compResults, setCompResults] = useState(false)
    const params = new URLSearchParams(location.search)
    let q = params.get('q')

    useEffect(() => {
        dispatch(getSearchSetsThunk(q)).then(() => dispatch(getSearchCompsThunk(q))).then(() => setIsLoaded(true))
    }, [dispatch, q, location])

    let searchSets = useSelector((state) => {
        if (isLoaded && state.sets) return Object.values(state.sets)
        else return []
    })

    let searchComps = useSelector((state) => {
        if (isLoaded && state.comparisons) return Object.values(state.comparisons)
        else return []
    })


    const openTop = () => {
        setTopResults(true)
        setSetResults(false)
        setCompResults(false)
    }

    const openSets = () => {
        setTopResults(false)
        setSetResults(true)
        setCompResults(false)
    }

    const openComps = () => {
        setTopResults(false)
        setSetResults(false)
        setCompResults(true)
    }

    return (
        <>{isLoaded && <div className='homepage-wrapper' >
            {topResults && <div className='login-signup-buttons-wrapper' id="search-button-wrapper">
                <div className='login-signup-wrapper'>
                    <button id='login-active' onClick={openTop}>Top results</button>
                    <i className="fa-solid fa-paintbrush" />
                </div>
                <div className='login-signup-wrapper'>
                    <button onClick={openSets}>Set results</button>
                </div>
                <div className='login-signup-wrapper'>
                    <button onClick={openComps}>Comparison results</button>
                </div>
            </div>}
            {setResults && <div className='login-signup-buttons-wrapper' id="search-button-wrapper">
                <div className='login-signup-wrapper'>
                    <button onClick={openTop}>Top results</button>
                </div>
                <div className='login-signup-wrapper'>
                    <button id='login-active' onClick={openSets}>Set results</button>
                    <i className="fa-solid fa-paintbrush" />
                </div>
                <div className='login-signup-wrapper'>
                    <button onClick={openComps}>Comparison results</button>
                </div>
            </div>}
            {compResults && <div className='login-signup-buttons-wrapper' id="search-button-wrapper">
                <div className='login-signup-wrapper'>
                    <button onClick={openTop}>Top results</button>
                </div>
                <div className='login-signup-wrapper'>
                    <button onClick={openSets}>Set results</button>
                </div>
                <div className='login-signup-wrapper'>
                    <button id='login-active' onClick={openComps}>Comparison results</button>
                    <i className="fa-solid fa-paintbrush" />
                </div>
            </div>}
            {topResults && <>{!searchSets.length && <h2>No set results</h2>}
                {!!searchSets.length && <><h2>Top set results</h2>
                    <div className='homepage-setcards-wrapper'>
                        {searchSets?.map((set, i) => {
                            if (i > 5) return
                            return <SetCard set={set} key={set.id} />
                        })}
                    </div></>}
                {!searchComps.length && <h2>No comparisons results</h2>}
                {!!searchComps.length && <><h2>Top comparison results</h2>
                    <div className='homepage-comparisons-wrapper'>
                        {searchComps?.map((comp, i) => {
                            if (i > 2) return
                            return <CompCard comp={comp} key={comp.id} />
                        })}
                    </div></>}
            </>}
            {setResults && <>{!searchSets.length && <h2>No set results</h2>}
                {!!searchSets.length && <><h2>All set results</h2>
                    <div className='homepage-setcards-wrapper'>
                        {searchSets?.map((set, i) => {
                            return <SetCard set={set} key={set.id} />
                        })}
                    </div></>}
            </>}
            {compResults && <>
                {!searchComps.length && <h2>No comparisons results</h2>}
                {!!searchComps.length && <><h2>All comparison results</h2>
                    <div className='homepage-comparisons-wrapper'>
                        {searchComps?.map((comp, i) => {
                            return <CompCard comp={comp} key={comp.id} />
                        })}
                    </div></>}
            </>}
        </div >}
        </>
    )
}

export default SearchPage
