import * as React from 'react';
import { View, Text, Button } from 'react-native';


function HomeScreen({ navigation }) {
    return(
        <View style = {{ flex: 1, alignItens:'center', justifyContent: 'center' }}>
            <Text>Home Screen</Text>
            <Button title='Ir para About' onPress={() => navigation.navigate('About')} />
        </View>
            
    );
}

export default HomeScreen;