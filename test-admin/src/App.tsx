
import { Admin, EditGuesser, ListGuesser, Resource } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import { UserList } from "./users";
import { PostCreate, PostEdit, PostList } from "./posts";
import PostIcon from "@mui/icons-material/Book";
import UserIcon from "@mui/icons-material/Group"
import { Dashboard } from "./Dashboard";
import { authProvider } from './authProvider'
import { myDataProvider } from "./myDataProvider"

/*const dataProvider = jsonServerProvider('https://jsonplaceholder.typicode.com');*/
const dataProvider = myDataProvider
const App = () => <Admin dataProvider={dataProvider} dashboard={Dashboard}> 
  <Resource name="drinks" list={ListGuesser} />
</Admin>;

export default App;
