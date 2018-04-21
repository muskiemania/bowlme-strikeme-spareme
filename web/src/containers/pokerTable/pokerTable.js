import React, { Component } from 'react';
import './pokerTable.less';

class PokerTable extends Component {
    render() {
        return (
            <div className='poker-table'>
                {this.props.children}
            </div>
        );
    }
}

export default PokerTable;
