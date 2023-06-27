import React from 'react';
 import { View, FlatList, StyleSheet, Text, StatusBar } from 'react-native';
 
 const DADOS = [
     {
     id: '1',
     descricao: 'TV Led 49',
     categoria_id: 1
     },
     {
     id: '4',
     descricao: 'Camisa Trilha',
     categoria_id: 2
     },
     {
     id: '4',
     descricao: 'Qualquer semelhança é mera coincidência',
     categoria_id: 3
     },
 ];
 
 const Item = ({ descricao }) => (
     <View style={styles.item}>
     <Text style={styles.title}>{descricao}</Text>
     </View>
 );
 
 const App = () => {
     const renderItem = ({ item }) => (
     <Item descricao={item.descricao} />
     );
 
     return (
     <View style={styles.container}>
         <FlatList
         data={DADOS}
         renderItem={renderItem}
         keyExtractor={item => item.id}
         />
     </View>
     );
 }
 
 const styles = StyleSheet.create({
     container: {
     flex: 1,
     marginTop: StatusBar.currentHeight || 0,
     },
     item: {
     backgroundColor: 'yellow',
     padding: 20,
     marginVertical: 8,
     marginHorizontal: 16,
     },
     title: {
     fontSize: 12,
     },
 });
 
 export default App; 