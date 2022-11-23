import { useState } from "react"
import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { getOneSetThunk } from "../../store/sets"

const SetPage = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setIsLoaded] = useState(false)
    const { setId } = useParams()

    let set = useSelector((state) => {
        if (state.sets) return state.sets[setId]
        else return null
    })

    useEffect(() => {
        if (!set) {
            dispatch(getOneSetThunk(setId)).then((res) => {
                if (res) setIsLoaded(true)
                else history.push('/404')
            })
        } else setIsLoaded(true)
    }, [set])

    return (
        <div className="set-page-wrapper">

        </div>
    )
}

export default SetPage
