import React from 'react';
import PropTypes from 'prop-types';
import './cardinality.less';
import _ from 'lodash';

const Cardinality = ((props) => {

    let {value} = props;

    let xlate = {};
    xlate['T'] = '=';

    let xlated = value;
    if(_.includes(['A','2','3','4','5','6','7','8','9','T','J','Q','K'], value)) {
        xlated = (value in xlate) ? xlate[value] : value;
    }

    return (
        <div className='cardinality'>
            <span>{xlated}</span>
        </div>
    );
});

Cardinality.propTypes = {
    value: PropTypes.string
};

export default Cardinality;
