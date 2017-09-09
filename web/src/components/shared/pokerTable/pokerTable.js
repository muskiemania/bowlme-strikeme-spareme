import React from 'react';
import {render} from 'react-dom';
import Immutable from 'immutable';
import MyHand from '../../myHand/myHand';
import Seats from '../../seats/seats';
import DrawCards from '../../drawCards/drawCards';
import './pokerTable.less';

export default class PokerTable extends React.Component {
    render() {
        let cards = ['AS','2D','3C','4H','5S','TH','JD','QC','KS','9C','7D'];
        
        return (
            <div className='poker-table'>
                <Seats players={Immutable.List()} />
                <MyHand cards={Immutable.fromJS(cards)} />
                <DrawCards cardsInHand={Immutable.fromJS(cards).size} />
            </div>
        );
    }
}

