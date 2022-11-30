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
        default:
            return state;
    }
}
