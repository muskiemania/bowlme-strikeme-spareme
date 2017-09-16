import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import Immutable from 'immutable';

import ScoreboardRow from '../shared/scoreboardRow/scoreboardRow';

class Scoreboard extends Component {

    render() {
        //let {players} = this.props;
        
        let players = Immutable.fromJS([
            { name: 'Justin', cards: ['AS','2D','3H'] },
            { name: 'Sarah', cards: ['2H','4H','6H','8H','JH'] },
            { name: 'Jenna', cards: ['KS','KD','KC','KH','7C'] }
        ]);
        
        return (
            <div className='scoreboard'>
            {
                players.map((player, i) => {
                    return <ScoreboardRow player={player} key={`player-${i}`} />
                })
            }
        </div>
        );        
    }
}

Scoreboard.propTypes = {
    players: ImmutablePropTypes.list
};

export default Scoreboard;
