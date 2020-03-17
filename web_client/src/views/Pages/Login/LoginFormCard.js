import React from 'react';
import {
	Button,
	Card,
	CardBody,
	Col,
	Form,
	Input,
	InputGroup,
	InputGroupAddon,
	InputGroupText,
	Row,
	Alert
} from 'reactstrap';

const LoginFormCard = (props) => {
	return (
		<Card className="p-4">
			<CardBody>
				<Form>
					<h1>Login</h1>
					<p className="text-muted">Sign In to your account</p>
					{props.loginError && (
						<Row>
							<Col xs="12">
								<Alert color="danger">Incorrect email or password.</Alert>
							</Col>
						</Row>
					)}
					<InputGroup className="mb-3">
						<InputGroupAddon addonType="prepend">
							<InputGroupText>
								<i className="icon-user" />
							</InputGroupText>
						</InputGroupAddon>
						<Input type="text" placeholder="Email" autoComplete="email" onChange={props.handleEmailChangeCallback} />
					</InputGroup>
					<InputGroup className="mb-4">
						<InputGroupAddon addonType="prepend">
							<InputGroupText>
								<i className="icon-lock" />
							</InputGroupText>
						</InputGroupAddon>
						<Input
							type="password"
							placeholder="Password"
							autoComplete="current-password"
							onChange={props.handlePasswordChangeCallback}
						/>
					</InputGroup>
					<Row>
						<Col xs="6">
							<Button color="primary" className="px-4" onClick={props.handleSubmitCallback}>
								Login
							</Button>
						</Col>
						<Col xs="6" className="text-right">
							<Button color="link" className="px-0">
								Forgot password?
							</Button>
						</Col>
					</Row>
				</Form>
			</CardBody>
		</Card>
	);
};

export default LoginFormCard;
