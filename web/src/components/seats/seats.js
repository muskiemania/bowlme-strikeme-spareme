import React from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import {render} from 'react-dom';

const Seats = ((props) => {

    return (
        <div>Seats</div>
    );

});

Seats.propTypes = {
    players: ImmutablePropTypes.list
};

export default Seats;
