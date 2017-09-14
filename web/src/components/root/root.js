import React from 'react'
import PropTypes from 'prop-types'
import { Provider } from 'react-redux'
import { Router, Route, browserHistory, IndexRoute} from 'react-router'

import PokerTable from '../../containers/pokerTable/pokerTable';
import PokerGame from '../../components/pokerGame/pokerGame';

const Root = ({ store }) => (
    <Provider store={store}>
        <Router history={browserHistory}>
            <Route path="/" component={PokerTable}>
            </Route>
            <Route path="/game/(:gameId)" component={PokerTable}>
                <IndexRoute component={PokerGame} />
            </Route>
            <Route path="/results/(:gameId)" component={PokerTable}>
            </Route>
        </Router>
    </Provider>
)

Root.propTypes = {
    store: PropTypes.object.isRequired
}

export default Root
