import { get, post } from '../helpers/http';

export const ITEMS_HAS_ERRORED = 'ITEMS_HAS_ERRORED'
export const ITEMS_IS_LOADING = 'ITEMS_IS_LOADING'
export const ITEMS_FETCH_DATA_SUCCESS = 'ITEMS_FETCH_DATA_SUCCESS'

export function isError(bool) {
    return {
        type: ITEMS_HAS_ERRORED,
        isErrored: bool
    };
}

export function isLoading(bool) {
    return {
        type: ITEMS_IS_LOADING,
        isLoading: bool
    };
}

export function fetchDataSuccess(data) {

    return {
        type: ITEMS_FETCH_DATA_SUCCESS,
	game: data
    };
}

export function pokerGameGetData(url) {
    return (dispatch) => {
        dispatch(isLoading(true));

	get(url)
	    .then((data) => {
		let playerStatusId = data.player && data.player.status && data.player.status.statusId || 0;
		console.log(playerStatusId);
		if(playerStatusId === 4) {
		    window.location.href = '/results/';
		}
		return data;
	    })
	    .then((data) => {
		dispatch(isLoading(false));
		return dispatch(fetchDataSuccess(data));
	    })
	    .catch((e) => {
		console.log(e);
		dispatch(isError(true));
	    });        
    };
}

export function pokerGamePostData(url, payload) {
    console.log('posting data...');
    return (dispatch) => {
	post(url, payload)
	    .then((data) => {
		console.log(data);
		let playerStatusId = data.player && data.player.status && data.player.status.statusId || 0;
		if(playerStatusId === 4) {
		    window.location.href = '/results/';
		}
		return data;
	    })
	    .then((data) => dispatch(fetchDataSuccess(data)))
	    .catch((e) => {
		console.log(e);
		dispatch(isError(true));
	    });
    };
}
