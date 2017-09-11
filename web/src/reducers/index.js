import { combineReducers } from 'redux';
import { cards, isError, isLoading } from './pokerGameReducers';

export default combineReducers({
    cards,
    isError,
    isLoading
});
