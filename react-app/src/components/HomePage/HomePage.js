
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
    const [toggleAbout, setToggleAbout] = useState(false)
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
            {isLoaded && <div className='homepage-wrapper'>
                <div className='homepage-header-wrapper'>
                    <h2>Featured sets</h2>
                    <button onClick={() => setToggleAbout(!toggleAbout)} className='about-this-page-button'>about</button>
                    {toggleAbout && <div className='about-drop-down'>
                        <h5>Welcome to Artest an Art History Flash Card and Study Site</h5>
                        <div className='about-section-wrapper'>
                            <h6>Home Page</h6>
                            <p>From the home page users can see featured sets/comparisons and navigate to set/comparison pages by clicking on featured items. Users can also see different set/comparison options by searching or navigating to your sets/your comparisons</p>
                        </div>
                        <div className='about-section-wrapper'>
                            <h6>Sets</h6>
                            <p>Sets are collections of flash cards where one side features a work of art and the other shows the artist, year, and title for the work of art. The creator of a set can also write and display notes on each card.</p>
                        </div>
                        <div className='about-section-wrapper'>
                            <h6>Comparisons</h6>
                            <p>Comparisons are a study tool for writing and posting essays comparing two works of art. A user chooses two works of art and writes an essay comparing and contrasting them. The creator of a comparison can use image annotations for creating and displaying visual notes.</p>
                        </div>
                    </div>}
                </div>
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
