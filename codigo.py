titanic_data['Pclass'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.title('Distribution of Passengers by Class')
plt.show()