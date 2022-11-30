import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { clearComps, getOneCompThunk } from "../../store/comparisons"

const EditComp = () => {
    const [compTitle, setCompTitle] = useState('')
    const [errors, setErrors] = useState([])
    const history = useHistory()
    const dispatch = useDispatch()
    const [isLoaded, setIsLoaded] = useState(false)
    const [workOneTitle, setWorkOneTitle] = useState('')
    const [workOneArtist, setWorkOneArtist] = useState('')
    const [workOneDisplayDate, setWorkOneDisplayDate] = useState('')
    const [workOneUrl, setWorkOneUrl] = useState('')
    const [workTwoTitle, setWorkTwoTitle] = useState('')
    const [workTwoArtist, setWorkTwoArtist] = useState('')
    const [workTwoDisplayDate, setWorkTwoDisplayDate] = useState('')
    const [workTwoUrl, setWorkTwoUrl] = useState('')
    const [comparisonText, setComparisonText] = useState('')
    const { compId } = useParams()

    let comp = useSelector((state) => {
        if (state.comparisons) return state.comparisons[compId]
        else return null
    })

    useEffect(() => {
        if (!comp) {
            dispatch(getOneCompThunk(compId)).then((res) => {
                if (res) setIsLoaded(true)
                else history.push('/404')
            })
        } else {
            setCompTitle(comp.title)
            setWorkOneTitle(comp.workOneTitle)
            setWorkOneArtist(comp.workOneArtist)
            setWorkOneDisplayDate(comp.workOneDisplayDate)
            setWorkOneUrl(comp.workOneImageUrl)
            setWorkTwoTitle(comp.workTwoTitle)
            setWorkTwoArtist(comp.workTwoArtist)
            setWorkTwoDisplayDate(comp.workTwoDisplayDate)
            setWorkTwoUrl(comp.workTwoImageUrl)
            setComparisonText(comp.comparisonText)
            setIsLoaded(true)
        }
    }, [comp, dispatch, history, compId])


    const user = useSelector((state) => state.session.user)
    console.log(isLoaded)
    useEffect(() => {
        if (isLoaded && (!user || user?.id != comp?.userId)) {
            history.push('/')
            return
        }
    }, [history, user, isLoaded])

    const handleSubmit = async (e) => {
        e.preventDefault()
        let errorsArr = []

        if (!compTitle || compTitle.length > 75) errorsArr.push('Comparison title must be between 1 and 75 characters')

        if (!workOneTitle || workOneTitle.length > 75) errorsArr.push(`Work one title must be between 1 and 75 characters`)
        if (!workOneArtist || workOneArtist.length > 75) errorsArr.push(`Work one artist name must be between 1 and 75 characters`)
        if (!workOneDisplayDate || workOneDisplayDate.length > 75) errorsArr.push(`Work one date must be between 1 and 50 characters`)
        if (!workOneUrl || workOneUrl.length > 2048 || !(workOneUrl.includes('.jpg') || workOneUrl.includes('.png'))) errorsArr.push(`Work one image url must be valid url that includes .jpg or .png`)
        if (!workTwoTitle || workTwoTitle.length > 75) errorsArr.push(`Work two title must be between 1 and 75 characters`)
        if (!workTwoArtist || workTwoArtist.length > 75) errorsArr.push(`Work two artist name must be between 1 and 75 characters`)
        if (!workTwoDisplayDate || workTwoDisplayDate.length > 75) errorsArr.push(`Work two date must be between 1 and 50 characters`)
        if (!workTwoUrl || workTwoUrl.length > 2048 || !(workTwoUrl.includes('.jpg') || workTwoUrl.includes('.png'))) errorsArr.push(`Work two image url must be valid url that includes .jpg or .png`)
        if (comparisonText && comparisonText.length > 3000) errorsArr.push(`Comparison essay must be less than 3000 characters`)
        if (errorsArr.length) {
            setErrors(errorsArr)
            return
        }


        const response = await fetch(`/api/comparisons/${compId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: compTitle,
                work_1_title: workOneTitle,
                work_1_artist: workOneArtist,
                work_1_image_url: workOneUrl,
                work_1_display_date: workOneDisplayDate,
                work_2_title: workTwoTitle,
                work_2_artist: workTwoArtist,
                work_2_image_url: workTwoUrl,
                work_2_display_date: workTwoDisplayDate,
                comparison_text: comparisonText
            })
        })

        if (response.ok) {
            const comparison = await response.json()
            setIsLoaded(false)
            await dispatch(clearComps())
            history.push(`/comparisons/${comparison.id}`)
        }
    }




    return (
        <>{isLoaded && <div className="new-set-page-wrapper">
            <h2>Edit {comp.title}</h2>
            <form onSubmit={handleSubmit} className="new-set-form">
                {errors.length > 0 && <ul className="form-errors">
                    {errors.map((error, idx) => <li key={idx}>{error}</li>)}
                </ul>}
                <div className="new-set-input-wrapper">
                    <input
                        type="text"
                        className="create-form-input"
                        value={compTitle}
                        onChange={(e) => setCompTitle(e.target.value)}
                        required
                        maxLength={75}
                    />
                    <span className="create-form-label">
                        Comparison title
                    </span>
                </div>
                <div className="form-cards-list-card-wrapper">
                    <div className="form-cards-list-card">
                        <div className='form-cards-list-card-left'>
                            <div className="card-num-wrapper">Work one</div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workOneTitle}
                                    onChange={(e) => setWorkOneTitle(e.target.value)}
                                    required
                                    maxLength={75}
                                />
                                <span className="create-form-card-label">
                                    Title
                                </span>
                            </div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workOneArtist}
                                    onChange={(e) => setWorkOneArtist(e.target.value)}
                                    required
                                    maxLength={75}
                                />
                                <span className="create-form-card-label">
                                    Artist name
                                </span>
                            </div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workOneDisplayDate}
                                    onChange={(e) => setWorkOneDisplayDate(e.target.value)}
                                    required
                                    maxLength={50}
                                />
                                <span className="create-form-card-label">
                                    Date
                                </span>
                            </div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workOneUrl}
                                    onChange={(e) => setWorkOneUrl(e.target.value)}
                                    required
                                    maxLength={2048}
                                />
                                <span className="create-form-card-label">
                                    Image url
                                </span>
                            </div>
                        </div>
                        <div className='form-cards-list-card-right'>
                            <img
                                className="form-set-page-card-list-image"
                                alt={workOneTitle}
                                src={workOneUrl}
                                onError={e => {
                                    e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                    e.onerror = null
                                }}
                            ></img>
                        </div>
                    </div>
                </div>
                <div className="form-cards-list-card-wrapper">
                    <div className="form-cards-list-card">
                        <div className='form-cards-list-card-left'>
                            <div className="card-num-wrapper">Work two</div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workTwoTitle}
                                    onChange={(e) => setWorkTwoTitle(e.target.value)}
                                    required
                                    maxLength={75}
                                />
                                <span className="create-form-card-label">
                                    Title
                                </span>
                            </div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workTwoArtist}
                                    onChange={(e) => setWorkTwoArtist(e.target.value)}
                                    required
                                    maxLength={75}
                                />
                                <span className="create-form-card-label">
                                    Artist name
                                </span>
                            </div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workTwoDisplayDate}
                                    onChange={(e) => setWorkTwoDisplayDate(e.target.value)}
                                    required
                                    maxLength={50}
                                />
                                <span className="create-form-card-label">
                                    Date
                                </span>
                            </div>
                            <div className="new-card-input-wrapper">
                                <input
                                    type="text"
                                    className="create-form-card-input"
                                    value={workTwoUrl}
                                    onChange={(e) => setWorkTwoUrl(e.target.value)}
                                    required
                                    maxLength={2048}
                                />
                                <span className="create-form-card-label">
                                    Image url
                                </span>
                            </div>
                        </div>
                        <div className='form-cards-list-card-right'>
                            <img
                                className="form-set-page-card-list-image"
                                alt={workTwoTitle}
                                src={workTwoUrl}
                                onError={e => {
                                    e.target.src = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
                                    e.onerror = null
                                }}
                            ></img>
                        </div>
                    </div>
                </div>
                <div className="new-card-input-wrapper">
                    <textarea
                        className="create-form-card-input-text-area"
                        id="comp-essay-input"
                        onChange={e => setComparisonText(e.target.value)}
                        value={comparisonText}
                        minLength={1}
                        maxLength={3000}
                    />
                    <span className="create-form-card-label">
                        Comparison essay
                    </span>
                </div>
                <button className="form-submit-button">Done</button>
            </form>
        </div>}</>
    )
}

export default EditComp
