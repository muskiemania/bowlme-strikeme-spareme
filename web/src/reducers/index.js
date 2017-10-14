import { combineReducers } from 'redux';
import { game, isError, isLoading } from './pokerGameReducers';

export default combineReducers({
    game,
    isError,
    isLoading
});
