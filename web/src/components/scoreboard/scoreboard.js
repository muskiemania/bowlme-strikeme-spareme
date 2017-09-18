import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import Immutable from 'immutable';

import ScoreboardRow from '../shared/scoreboardRow/scoreboardRow';

import './scoreboard.less';

class Scoreboard extends Component {

    render() {
        //let {players} = this.props;
        
        let players = Immutable.fromJS([
            { name: 'Justin', cards: ['AS','2D','3H'], handDetails: { rank: 3, title: 'High Card' } },
            { name: 'Sarah', cards: ['2H','4H','6H','8H','JH'], handDetails: { rank: 2, title: 'Flush' } },
            { name: 'Jenna', cards: ['KS','KD','KC','KH','7C'], handDetails: { rank: 1, title: 'Four-Of-A-Kind' } }
        ]);
        
        return (
            <div className='scoreboard'>
            {
                players.sortBy(player => player.get('handDetails').get('rank')).map((player, i) => {
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
