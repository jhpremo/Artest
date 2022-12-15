const GET_COMPS = 'comps/get'

const getComps = (compObj) => {
    return {
        type: GET_COMPS,
        comps: compObj.comparisons
    }
}

export const getFeaturedCompsThunk = () => async (dispatch) => {
    const response = await fetch('/api/comparisons/featured')

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getComps(data));
    }
}

export const getSessionCompsThunk = () => async (dispatch) => {
    const response = await fetch('/api/comparisons/session')

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getComps(data));
    }
}

export const getSearchCompsThunk = (q) => async (dispatch) => {
    const response = await fetch(`/api/comparisons/search?q=${q}`)

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getComps(data));
    }
}

export const getOneCompThunk = (id) => async (dispatch) => {
    const response = await fetch(`/api/comparisons/${id}`)

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        dispatch(getComps(data));
        return true
    } else return false
}

const CLEAR_COMPS = 'comparisons/clear/store'

export const clearComps = () => {
    return {
        type: CLEAR_COMPS
    }
}

const UPDATE_MARKER_ONE = "comparisons/markerobj/update/one"

const updateMarkerOne = (compId, markerObj) => {
    return {
        type: UPDATE_MARKER_ONE,
        markerObj: markerObj,
        compId
    }
}

const UPDATE_MARKER_TWO = "comparisons/markerobj/update/two"

const updateMarkerTwo = (compId, markerObj) => {
    return {
        type: UPDATE_MARKER_TWO,
        markerObj: markerObj,
        compId
    }
}

export const updateMarkerThunk = (compId, markerObj, imgId) => async (dispatch) => {
    let work_1_marker_obj
    let work_2_marker_obj
    if (imgId === "img1") work_1_marker_obj = markerObj
    if (imgId === "img2") work_2_marker_obj = markerObj

    const response = await fetch(`/api/comparisons/${compId}/marker`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            work_1_marker_obj,
            work_2_marker_obj
        })
    })

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }
        if (work_1_marker_obj) dispatch(updateMarkerOne(compId, work_1_marker_obj));
        else if (work_2_marker_obj) dispatch(updateMarkerTwo(compId, work_2_marker_obj))
        return true
    } else return false
}


export default function compsReducer(state = null, action) {
    switch (action.type) {
        case GET_COMPS:
            let getCompsState = {}
            for (let i = 0; i < action.comps.length; i++) {
                getCompsState[action.comps[i].id] = action.comps[i]
            }
            return getCompsState
        case CLEAR_COMPS:
            return null
        case UPDATE_MARKER_ONE:
            let compsState = { ...state }
            compsState[action.compId].workOneMarkerObj = JSON.stringify(action.markerObj)
            return compsState
        case UPDATE_MARKER_TWO:
            let twoCompsState = { ...state }
            twoCompsState[action.compId].workTwoMarkerObj = JSON.stringify(action.markerObj)
            return twoCompsState
        default:
            return state;
    }
}
