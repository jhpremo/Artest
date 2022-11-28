const UPDATE_SET_ITEM = 'update/set/list/form'

export const updateListItem = (cardObj, index) => {
    return {
        type: UPDATE_SET_ITEM,
        cardObj: cardObj,
        index: index
    }
}

const ADD_SET_CARD = 'update/set/list/form/add/card'

export const formAddCard = () => {
    return {
        type: ADD_SET_CARD
    }
}



const DELETE_SET_CARD = 'update/set/list/form/delete/card'

export const formDeleteCard = (index) => {
    return {
        type: DELETE_SET_CARD,
        index: index
    }
}

const RESET_SET_FORM = 'set/form/reset'

export const formReset = () => {
    return {
        type: RESET_SET_FORM
    }
}

let initialState = [
    {
        title: '',
        artist: '',
        displayDate: '',
        url: '',
        notes: ''
    },
    {
        title: '',
        artist: '',
        displayDate: '',
        url: '',
        notes: ''
    },
    {
        title: '',
        artist: '',
        displayDate: '',
        url: '',
        notes: ''
    },
    {
        title: '',
        artist: '',
        displayDate: '',
        url: '',
        notes: ''
    }]

export default function setFormReducer(state = initialState, action) {
    switch (action.type) {
        case UPDATE_SET_ITEM:
            let newState = [...state]
            newState[action.index] = action.cardObj
            return newState
        case ADD_SET_CARD:
            let addState = [...state]
            addState.push({
                title: '',
                artist: '',
                displayDate: '',
                url: '',
                notes: ''
            })
            return addState
        case DELETE_SET_CARD:
            let deleteState = [...state]
            deleteState.splice(action.index, 1)
            return deleteState
        case RESET_SET_FORM:
            let resetState = [...initialState]
            return resetState
        default:
            return state;
    }
}
