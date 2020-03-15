import firebase from 'firebase';
import 'firebase/auth';
import 'firebase/firestore';

type config = {
	apiKey: string | undefined;
	authDomain: string | undefined;
	databaseURL: string | undefined;
	projectId: string | undefined;
	storageBucket: string | undefined;
	messagingSenderId: string | undefined;
	appId: string | undefined;
	measurementId: string | undefined;
};

// configuration
const firebaseConfig: config = {
	apiKey: process.env.REACT_APP_API_KEY,
	authDomain: process.env.REACT_APP_AUTH_DOMAIN,
	databaseURL: process.env.REACT_APP_DATABASE_URL,
	projectId: process.env.REACT_APP_PROJECT_ID,
	storageBucket: process.env.REACT_APP_STORAGE_BUCKET,
	messagingSenderId: process.env.REACT_APP_MESSAGING_SENDER_ID,
	appId: process.env.REACT_APP_APP_ID,
	measurementId: process.env.REACT_APP_MEASUREMENT_ID
};

// Initialize Firebase
export const rulebloxFirebase = firebase.initializeApp(firebaseConfig);
rulebloxFirebase.analytics();

// Initialize cloud firestore
const baseDb = rulebloxFirebase.firestore();
export const db = baseDb;
