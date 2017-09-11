import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './button.less';

const Button = ((props) => {

    let {text} = props;

    return (
        <div className='draw-button'>
        <a href='#' className='button'>
        <div className='inner-box'>
        {text}
        </div>
        </a>
        </div>
    );
});

Button.propTypes = {
    text: PropTypes.string
};

export default Button;
