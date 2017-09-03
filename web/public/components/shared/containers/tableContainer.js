import React, {PropTypes} from 'react';

class TableContainer extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className='table-container'>
                {this.props.children}
            </div>
        )
    }
}

export default TableContainer;
    

    
