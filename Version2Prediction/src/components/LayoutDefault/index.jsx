import Footer from './Footer';
import Header from './Header';
import Main from './Main';

function LayoutDefault() {
  return (
    <>
      <header>
        <Header />
      </header>
      <main>
        <Main />
      </main>
      <footer>
        <Footer />
      </footer>
    </>
  );
}
export default LayoutDefault;
