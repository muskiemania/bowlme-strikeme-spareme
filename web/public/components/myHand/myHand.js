import React from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import {render} from 'react-dom';
//import './myHand.less';
import _ from 'lodash';
import Cards from '../shared/cards/cards';

const MyHand = ((props) => {

    let {cards} = props;

    return (
        <div className='grid-x row'>
            <div className='small-12 columns'>
                <div className='grid-x row align-center'>
                    <Cards cards={cards} />
                </div>
            </div>
        </div>
    );
});

MyHand.propTypes = {
    cards: ImmutablePropTypes.list
};

export default MyHand;

