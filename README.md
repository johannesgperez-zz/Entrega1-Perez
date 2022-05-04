# VentaPermutaIMs
##### v:1.0

### Objetivo del Portal:

#### Venta y permuta de instrumentos musicales. Los usuarios en el portal pueden consultar cuales instrumentos están listados y con la posibilidad de contactar a través de via telefónica el instrumento que sea de su interés. Adicionalmente los usuarios pueden agregar a la BD,instrumentos musicales que quieran vender o permutar. Por último está la posibilidad de buscar marcas de instrumenos musicales alojados en la BD.


### Navbar:

#### El Navbar consta de las secciones: Inicio (Padre Html), Guitarras, Bajos, Pedales, Amplificadores


### Para agregar items a la base de datos se puede realizar desde las secciones antes mencionadas o también a través de las siguientes urls:

#### Guitarras: http://127.0.0.1:8000/guitarraformulario

#### Bajos: http://127.0.0.1:8000/bajoformulario

#### Pedales: http://127.0.0.1:8000/pedalformulario

#### Amplificadores: http://127.0.0.1:8000/ampliformulario


### Para buscar un instrumento por su marca se hace a través del siguiente link, el cual a su vez está incluido en el html padre y de igual forma se muestra en todas las secciones:

####  http://127.0.0.1:8000/busquedaInstrumento


### Los Modelos de la BD son los siguientes:

#### Guitarra: Contiene las columnas marca, modelo, anio, cuerdas, descripcion, precio, telefono_contacto

#### Bajo: Contiene las columnas marca, modelo, anio, cuerdas, descripcion, precio, telefono_contacto

#### Pedal: Contiene las columnas marca, tipo_efecto, anio, descripcion, precio, telefono_contacto

#### Amplificador: Contiene las columnas marca, tipo_amplificador, anio, descripcion, precio, telefono_contacto
