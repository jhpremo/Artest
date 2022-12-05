import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"

const NewComp = () => {
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

    const user = useSelector((state) => state.session.user)
    useEffect(() => {
        if (!user) {
            history.push('/')
            return
        }
    }, [history, user])

    const handleSubmit = async (e) => {
        e.preventDefault()
        let errorsArr = []

        if (!compTitle || compTitle.length > 75) errorsArr.push('Comparison title must be between 1 and 75 characters')

        if (!workOneTitle || workOneTitle.length > 75) errorsArr.push(`Work one title must be between 1 and 75 characters`)
        if (!workOneArtist || workOneArtist.length > 75) errorsArr.push(`Work one artist name must be between 1 and 75 characters`)
        if (!workOneDisplayDate || workOneDisplayDate.length > 75) errorsArr.push(`Work one date must be between 1 and 50 characters`)
        if (!workOneUrl || workOneUrl.length > 2048 || !(workOneUrl.toLowerCase().includes('.jpg') || workOneUrl.toLowerCase().includes('.png'))) errorsArr.push(`Work one image url must be valid url that includes .jpg or .png`)
        if (!workTwoTitle || workTwoTitle.length > 75) errorsArr.push(`Work two title must be between 1 and 75 characters`)
        if (!workTwoArtist || workTwoArtist.length > 75) errorsArr.push(`Work two artist name must be between 1 and 75 characters`)
        if (!workTwoDisplayDate || workTwoDisplayDate.length > 75) errorsArr.push(`Work two date must be between 1 and 50 characters`)
        if (!workTwoUrl || workTwoUrl.length > 2048 || !(workTwoUrl.toLowerCase().includes('.jpg') || workTwoUrl.toLowerCase().includes('.png'))) errorsArr.push(`Work two image url must be valid url that includes .jpg or .png`)
        if (comparisonText && comparisonText.length > 3000) errorsArr.push(`Comparison essay must be less than 3000 characters`)
        if (errorsArr.length) {
            setErrors(errorsArr)
            return
        }


        const response = await fetch('/api/comparisons', {
            method: 'POST',
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
            history.push(`/comparisons/${comparison.id}`)
        }
    }




    return (
        <div className="new-set-page-wrapper">
            <h2>Create a new art comparison</h2>
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
                                    Title e.g "Hades abducting persephone amphora"
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
                                    Artist name e.g "Andokides Painter"
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
                                    Display Date e.g "6th century B.C.E."
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
                                    Title e.g "Roman terra sigillata bowl"
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
                                    Artist name e.g "Unknown roman artist"
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
                                    Display Date e.g "1st century C.E."
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

                <button className="form-submit-button">Create</button>
            </form>
        </div>
    )
}

export default NewComp
