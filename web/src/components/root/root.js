import React from 'react'
import PropTypes from 'prop-types'
import { Provider } from 'react-redux'
import { Router, Route, browserHistory, IndexRoute} from 'react-router'

import PokerTable from '../../containers/pokerTable/pokerTable';
import PokerGame from '../pokerGame/pokerGame';
import JoinCreate from '../joinCreate/joinCreate';
import Scoreboard from '../scoreboard/scoreboard';

import './root.less';

const Root = ({ store }) => (
    <Provider store={store}>
        <Router history={browserHistory}>
            <Route path="/" component={PokerTable}>
                <IndexRoute component={JoinCreate} />
            </Route>
            <Route path="/game/" component={PokerTable}>
                <IndexRoute component={PokerGame} />
            </Route>
            <Route path="/results/" component={PokerTable}>
                <IndexRoute component={Scoreboard} />
            </Route>
        </Router>
    </Provider>
)

Root.propTypes = {
    store: PropTypes.object.isRequired
}

export default Root
