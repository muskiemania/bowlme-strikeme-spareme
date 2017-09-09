import React from 'react';
import PropTypes from 'prop-types';
import './suit.less';

const Suit = ((props) => {

    let {value} = props;

    let xlate = {};
    xlate['clubs'] = ']';
    xlate['diamonds'] = '[';
    xlate['hearts'] = '{';
    xlate['spades'] = '}';

    let xlated = value;
    if(value in xlate) {
        xlated = xlate[value];
    }
    
    return (
        <div className='suit'>
            <span>{xlated}</span>
        </div>
    );
});

Suit.propTypes = {
    value: PropTypes.string
};

export default Suit;
