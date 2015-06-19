import mock
import testtools

import shellper.base as main_base
import shellper.main as main_function
import shellper.tests.unit.fake_class as base


class TestMain(testtools.TestCase):
    @mock.patch('shellper.base.Base.create_event', return_value=None)
    @mock.patch('shellper.base.Base.search_query', return_value=None)
    @mock.patch('shellper.base.Base.get_event_list', return_value=['event1',
                                                                   'event2'])
    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=base.FakeClass())
    @mock.patch('shellper.validation.validate')
    def test_main_with_events(self, mock_validate, mock_argparse, mock_getlist,
                              mock_query, mock_create):
        main_function.main()

    @mock.patch('shellper.base.Base.create_event', return_value=None)
    @mock.patch('shellper.base.Base.search_query', return_value=None)
    @mock.patch('shellper.base.Base.get_event_list', return_value=[])
    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=base.FakeClass())
    @mock.patch('shellper.validation.validate')
    def test_main_without_events(self, mock_validate, mock_argparse,
                                 mock_getlist, mock_query, mock_create):
        main_function.main()

    @mock.patch('shellper.base.Base.search_query', return_value=True)
    def test_add_links_with_results(self, mock_query):
        config = [{
            'time': '22:00',
            'date': '18.05.2015',
            'summary': 'How clone git repository?'
        }]
        main_function.add_links(main_base.Base(), config)

    @mock.patch('shellper.base.Base.search_query', return_value=None)
    def test_add_links_without_results(self, mock_query):
        config = [{
            'time': '22:00',
            'date': '18.05.2015',
            'summary': 'How clone git repository?'
        }]
        main_function.add_links(main_base.Base(), config)
