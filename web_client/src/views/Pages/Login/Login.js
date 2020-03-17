import React, { Component } from 'react';
import { CardGroup, Col, Container, Row } from 'reactstrap';
import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom';

import { loginUser } from '../../../actions';
import LoginFormCard from './LoginFormCard';
import SignUpCard from './SignUpCard';

class Login extends Component {
	state = { email: '', password: '' };
	handleEmailChange = ({ target }) => {
		this.setState({ email: target.value });
	};

	handlePasswordChange = ({ target }) => {
		this.setState({ password: target.value });
	};

	handleSubmit = () => {
		const { dispatch } = this.props;
		const { email, password } = this.state;

		dispatch(loginUser(email, password));
	};

	render() {
		const { loginError, isAuthenticated } = this.props;
		if (isAuthenticated) {
			return <Redirect to="/" />;
		} else {
			return (
				<div className="app flex-row align-items-center">
					<Container>
						<Row className="justify-content-center">
							<Col md="8">
								<CardGroup>
									<LoginFormCard
										loginError={loginError}
										handleSubmitCallback={this.handleSubmit}
										handlePasswordChangeCallback={this.handlePasswordChange}
										handleEmailChangeCallback={this.handleEmailChange}
									/>
									<SignUpCard />
								</CardGroup>
							</Col>
						</Row>
					</Container>
				</div>
			);
		}
	}
}

const mapStateToProps = (state) => {
	return {
		isLoggingIn: state.auth.isLoggingIn,
		loginError: state.auth.loginError,
		isAuthenticated: state.auth.isAuthenticated
	};
};

export default connect(mapStateToProps)(Login);
