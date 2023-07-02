import * as React from 'react';
 import { View, Text } from 'react-native';
 import { NavigationContainer } from '@react-navigation/native';
 import { createDrawerNavigator } from '@react-navigation/drawer';
 
 import HomeScreen from './screens/home';
 import AboutScreen from './screens/about';
 
 const Drawer = createDrawerNavigator();
 
 function App() {
     return (
     <NavigationContainer>
         <Drawer.Navigator initialRouteName='Home'>
         <Drawer.Screen name='Home' component={HomeScreen} />
         <Drawer.Screen name='About' component={AboutScreen} />
         </Drawer.Navigator>
     </NavigationContainer>
     );
 }
 
 export default App;